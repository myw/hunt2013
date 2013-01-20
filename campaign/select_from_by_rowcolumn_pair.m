function selected = select_from_by_rowcolumn_pair(cell_array, rows, columns)
    n = length(rows);
    selected = cell(1,n);

    for ix = 1:n
        selected(ix) = cell_array(rows(ix), columns(ix));
    end
end
